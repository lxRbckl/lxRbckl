"use strict";
var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var __async = (__this, __arguments, generator) => {
  return new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e) {
        reject(e);
      }
    };
    var rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e) {
        reject(e);
      }
    };
    var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });
};

// src/index.ts
var src_exports = {};
__export(src_exports, {
  dirDel: () => dirDel,
  dirGet: () => dirGet,
  dirSet: () => dirSet,
  fileDel: () => fileDel,
  fileGet: () => fileGet,
  fileSet: () => fileSet,
  getProjectPath: () => getProjectPath,
  ocotkit: () => ocotkit,
  openai: () => openai
});
module.exports = __toCommonJS(src_exports);

// src/local.ts
var import_path = __toESM(require("path"));
var import_promises = require("fs/promises");
function getProjectPath(file = "", delimeter = "/") {
  const dir = import_path.default.dirname(__filename).split(/[]/);
  const base = dir.includes("node_modules") ? -4 : -1;
  return [...dir.slice(0, base), file.split(/[/\\]/)].join(delimeter);
}
function fileSet(_0, _1) {
  return __async(this, arguments, function* (data, file, indent = 3, path2 = getProjectPath()) {
    try {
      yield (0, import_promises.writeFile)(
        path2 + file,
        file.endsWith(".json") ? JSON.stringify(data, null, indent) : data
      );
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + file}`);
    }
  });
}
function fileGet(_0) {
  return __async(this, arguments, function* (file, path2 = getProjectPath(), encoding = "utf8") {
    try {
      const fin = yield (0, import_promises.readFile)(path2 + file, encoding);
      return file.endsWith(".json") ? JSON.parse(fin.toString()) : fin;
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + file}`);
    }
  });
}
function fileDel(_0) {
  return __async(this, arguments, function* (file, path2 = getProjectPath()) {
    try {
      yield (0, import_promises.unlink)(path2 + file);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + file}`);
    }
  });
}
function dirSet(_0) {
  return __async(this, arguments, function* (dir, path2 = getProjectPath()) {
    try {
      yield (0, import_promises.mkdir)(path2 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + dir}`);
    }
  });
}
function dirGet(_0) {
  return __async(this, arguments, function* (dir, path2 = getProjectPath()) {
    try {
      return yield (0, import_promises.readdir)(path2 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + dir}`);
    }
  });
}
function dirDel(_0) {
  return __async(this, arguments, function* (dir, path2 = getProjectPath()) {
    try {
      yield (0, import_promises.rmdir)(path2 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path2 + dir}`);
    }
  });
}

// src/openai.ts
var import_util = require("util");
var import_child_process = require("child_process");
var openai = class {
  constructor(token, model = "gpt-4o", temperature = 1.5) {
    this._model = model;
    this._token = token;
    this._temperature = temperature;
  }
  query(prompt) {
    return __async(this, null, function* () {
      const query = `
      
         curl -X POST https://api.openai.com/v1/chat/completions             -H "Content-Type: application/json"             -H "Authorization: Bearer ${this._token}"             -d '{
                  "model" : "${this._model}",
                  "temperature" : ${this._temperature},
                  "messages" : [
                     {
                        "role" : "system",
                        "content" : "You are a helpful assistant."
                     },
                     {
                        "role" : "user",
                        "content" : "${prompt}"
                     }
                  ]
               }'
      
      `;
      const execPromise = (0, import_util.promisify)(import_child_process.exec);
      const { stdout, stderr } = yield execPromise(query);
      return JSON.parse(stdout).choices[0].message.content;
    });
  }
};

// src/octokit.ts
var import_rest = require("@octokit/rest");
var ocotkit = class {
  constructor(token, owner, indent = 3, stringEncoding = "utf8", bufferEncoding = "base64") {
    this.urlFileGet = (repo, file) => `GET /repos/${this._owner}/${repo}/contents/${file}`;
    this.urlFilePut = (repo, file) => `PUT /repos/${this._owner}/${repo}/contents/${file}`;
    this._token = token;
    this._owner = owner;
    this._indent = indent;
    this._stringEncoding = stringEncoding;
    this._bufferEncoding = bufferEncoding;
    this._octokit = new import_rest.Octokit({ auth: this._token });
  }
  repositoryGet(file, branch, repository, property = "content", suppressError = false) {
    return __async(this, null, function* () {
      let fileGet2 = this.urlFileGet(repository, file);
      try {
        let data = (yield this._octokit.request(fileGet2, { ref: branch })).data;
        switch (property == "content") {
          case false:
            return data[property];
          case true:
            let encoding = data.encoding;
            let buffer = Buffer.from(data.content, encoding);
            return JSON.parse(buffer.toString(this._stringEncoding));
        }
      } catch (error) {
        suppressError ? console.log("Error: ", error, "\nQuery: ", fileGet2, "\nBranch: ", branch) : void 0;
        return false;
      }
    });
  }
  respositorySet(data, file, branch, repository, suppressError = false, message = "Automated Action") {
    return __async(this, null, function* () {
      let filePut = this.urlFilePut(repository, file);
      try {
        yield this._octokit.request(filePut, {
          branch,
          message,
          owner: this._owner,
          sha: yield this.repositoryGet(file, branch, repository, "sha", suppressError),
          content: Buffer.from(JSON.stringify(data, null, this._indent)).toString(this._bufferEncoding)
        });
        return true;
      } catch (error) {
        suppressError ? console.log("Error: ", error, "\nQuery: ", filePut, "\nBranch: ", branch) : void 0;
        return false;
      }
    });
  }
};
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  dirDel,
  dirGet,
  dirSet,
  fileDel,
  fileGet,
  fileSet,
  getProjectPath,
  ocotkit,
  openai
});
