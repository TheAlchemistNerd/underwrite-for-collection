import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import {renderMermaid} from 'file:///C:/Users/Nevo/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/src/index.js';
const req=createRequire('C:/Users/Nevo/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/src/index.js');
const puppeteer=req('puppeteer');
const dir=path.dirname(fileURLToPath(import.meta.url));
const config=JSON.parse(await fs.readFile(path.join(dir,'MONIEPOINT_WORKFLOW_MERMAID_CONFIG.json'),'utf8'));
const browserConfig=JSON.parse((await fs.readFile(path.join(dir,'MONIEPOINT_WORKFLOW_PUPPETEER_CONFIG.json'),'utf8')).replace(/^\uFEFF/,''));
const names=['MONIEPOINT_GOVERNED_AGENTIC_CREDIT_WORKFLOW','MONIEPOINT_WORKFLOW_01_EVIDENCE_AND_CALCULATIONS','MONIEPOINT_WORKFLOW_02_APPROVAL_AND_EXECUTION','MONIEPOINT_WORKFLOW_03_MONITORING_AND_LEARNING'];
const browser=await puppeteer.launch(browserConfig);
try {
 for(const name of names){
  const definition=await fs.readFile(path.join(dir,name+'.mmd'),'utf8');
  for(const format of ['svg','png']){
   const {data}=await renderMermaid(browser,definition,format,{viewport:{width:2400,height:4000,deviceScaleFactor:1},backgroundColor:'white',mermaidConfig:config});
   await fs.writeFile(path.join(dir,name+'.'+format),data);
   console.log(name+'.'+format+' saved');
  }
 }
} finally {await browser.close();}
