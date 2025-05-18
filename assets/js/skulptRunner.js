function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function runCode() {
  let prog = document.getElementById("code").value;
  let output = document.getElementById("output");
  Sk.pre = "output";
  Sk.configure({ output: (text) => output.innerHTML += text, read: builtinRead });
  (Sk.misceval.asyncToPromise(() => Sk.importMainWithBody("<stdin>", false, prog)))
    .catch(e => output.innerHTML = e.toString());
}
