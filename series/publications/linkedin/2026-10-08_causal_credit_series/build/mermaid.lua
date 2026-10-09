-- Render Mermaid blocks to named standalone assets and embed them in a combined PDF.
local sep = package.config:sub(1,1)
local outdir = os.getenv("MERMAID_OUTDIR") or error("MERMAID_OUTDIR is required")
local names, captions, covers, cover_captions = {}, {}, {}, {}
local function split_pipe(s)
  local result = {}
  for item in string.gmatch(s or "", "([^|]+)") do table.insert(result, item) end
  return result
end
names = split_pipe(os.getenv("MERMAID_NAMES"))
captions = split_pipe(os.getenv("MERMAID_CAPTIONS"))
covers = split_pipe(os.getenv("MERMAID_COVER_NAMES"))
cover_captions = split_pipe(os.getenv("MERMAID_COVER_CAPTIONS"))
local article = os.getenv("MERMAID_ARTICLE") or "underwrite_for_collection"
local image_prefix = os.getenv("MERMAID_IMAGE_PREFIX") or "linkedin_diagrams/"
local sequence = 0
local definitions = {}
local reuse_assets = true
local function join(a,b) return a .. sep .. b end
local function quote(s) return '"' .. s:gsub('"', '\\"') .. '"' end
local function write_file(path, content)
  local f = assert(io.open(path, "wb")); f:write(content); f:close()
end
local function is_mermaid(el)
  for _, class in ipairs(el.classes) do if class == "mermaid" then return true end end
  local first = el.text:match("^%s*([^\r\n]+)") or ""
  return first:match("^flowchart%s") or first:match("^graph%s") or first:match("^stateDiagram") or first:match("^sequenceDiagram") or first:match("^journey%s") or first:match("^mindmap%s")
end
local function run_mmdc(input, output)
  local config = os.getenv("MERMAID_PUPPETEER_CONFIG")
  local cmd = "mmdc -i " .. quote(input) .. " -o " .. quote(output) .. " -b white -t neutral -s 2 -q"
  if config then cmd = cmd .. " -p " .. quote(config) end
  local ok, why, code = os.execute(cmd)
  if not (ok == true or ok == 0 or code == 0) then error("mmdc failed for " .. input .. ": " .. tostring(why) .. " " .. tostring(code)) end
end
function CodeBlock(el)
  if not is_mermaid(el) then return nil end
  sequence = sequence + 1
  local name = names[sequence] or string.format("%s_diagram_%02d", article, sequence)
  local caption = captions[sequence] or name:gsub("_", " ")
  local mmd = join(outdir, name .. ".mmd")
  local old = io.open(mmd, "rb")
  if old then
    if old:read("*a") ~= el.text .. "\n" then reuse_assets = false end
    old:close()
  else reuse_assets = false end
  for _, ext in ipairs({"png", "svg"}) do
    local existing = io.open(join(outdir, name .. "." .. ext), "rb")
    if existing then existing:close() else reuse_assets = false end
  end
  write_file(mmd, el.text .. "\n")
  table.insert(definitions, "```mermaid\n" .. el.text .. "\n```\n")
  return pandoc.RawBlock("latex", "\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.92\\linewidth,height=0.72\\textheight,keepaspectratio]{" .. image_prefix .. name .. ".png}\n\\caption{" .. caption .. "}\n\\end{figure}")
end
function Str(el)
  local missing = {[0x2208]=true,[0x223C]=true,[0x204E]=true,[0x2AEB]=true}
  local result, buffer = pandoc.List(), ""
  for _, cp in utf8.codes(el.text) do
    local ch = utf8.char(cp)
    if missing[cp] then
      if #buffer > 0 then result:insert(pandoc.Str(buffer)); buffer = "" end
      if cp == 0x204E then
        result:insert(pandoc.RawInline("latex", "\\ensuremath{\\ast}"))
      else
        result:insert(pandoc.RawInline("latex", "{\\normalfont\\fontspec{Cambria Math}" .. ch .. "}"))
      end
    else buffer = buffer .. ch end
  end
  if #buffer > 0 then result:insert(pandoc.Str(buffer)) end
  return result
end
function Pandoc(doc)
  local batch = join(outdir, "all_diagrams.md")
  write_file(batch, table.concat(definitions, "\n"))
  if not reuse_assets then
  for _, ext in ipairs({"png", "svg"}) do
    run_mmdc(batch, join(outdir, "render." .. ext))
    for i=1,sequence do
      local rendered = join(outdir, "render-" .. i .. "." .. ext)
      local f = assert(io.open(rendered, "rb"))
      local bytes = f:read("*a"); f:close()
      write_file(join(outdir, names[i] .. "." .. ext), bytes)
      os.remove(rendered)
    end
  end
  end
  return doc
end
-- The in-body figures provide one copy of each diagram in reading order.
function unused_cover_insertion(doc)
  local blocks = pandoc.List()
  local article_index = 0
  for _, block in ipairs(doc.blocks) do
    blocks:insert(block)
    if block.t == "Header" and block.level == 1 and article_index < #covers then
      article_index = article_index + 1
      local name = covers[article_index]
      local caption = cover_captions[article_index] or name:gsub("_", " ")
      local image = pandoc.Image(caption, image_prefix .. name .. ".png", "", {width="92%"})
      blocks:insert(pandoc.Para({image}))
    end
  end
  doc.blocks = blocks
  return doc
end
