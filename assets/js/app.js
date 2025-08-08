function resetOutput(outId){const out=document.getElementById(outId);if(out) out.textContent='';}
function outfFactory(outId){return function(text){const out=document.getElementById(outId);if(out) out.textContent += text;}}
function builtinRead(x){if(Sk.builtinFiles===undefined||Sk.builtinFiles['files'][x]===undefined){throw "File not found: '"+x+"'";}return Sk.builtinFiles['files'][x];}
async function runSkulpt(codeId,outId){const code=document.getElementById(codeId)?.value||'';const out=document.getElementById(outId);if(!out) return;out.textContent='';try{Sk.configure({output:outfFactory(outId),read:builtinRead});await Sk.importMainWithBody('<stdin>',false,code,true);}catch(e){out.textContent=String(e);}}
(function(){const y=document.getElementById('year');if(y){y.textContent=String(new Date().getFullYear());}})();
