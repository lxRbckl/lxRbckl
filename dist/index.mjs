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

// node_modules/tsup/assets/esm_shims.js
import { fileURLToPath } from "url";
import path from "path";
var import_meta = {};
var getFilename = () => fileURLToPath(import_meta.url);
var __filename = /* @__PURE__ */ getFilename();

// src/local.ts
import path2 from "path";
import {
  mkdir,
  rmdir,
  unlink,
  readdir,
  readFile,
  writeFile
} from "fs/promises";
function getProjectPath(file = "", delimeter = "/") {
  const dir = path2.dirname(__filename).split(/[]/);
  const base = dir.includes("node_modules") ? -4 : -1;
  return [...dir.slice(0, base), file.split(/[/\\]/)].join(delimeter);
}
function fileSet(_0, _1) {
  return __async(this, arguments, function* (data, file, indent = 3, path3 = getProjectPath()) {
    try {
      yield writeFile(
        path3 + file,
        file.endsWith(".json") ? JSON.stringify(data, null, indent) : data
      );
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + file}`);
    }
  });
}
function fileGet(_0) {
  return __async(this, arguments, function* (file, path3 = getProjectPath(), encoding = "utf8") {
    try {
      const fin = yield readFile(path3 + file, encoding);
      return file.endsWith(".json") ? JSON.parse(fin.toString()) : fin;
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + file}`);
    }
  });
}
function fileDel(_0) {
  return __async(this, arguments, function* (file, path3 = getProjectPath()) {
    try {
      yield unlink(path3 + file);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + file}`);
    }
  });
}
function dirSet(_0) {
  return __async(this, arguments, function* (dir, path3 = getProjectPath()) {
    try {
      yield mkdir(path3 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + dir}`);
    }
  });
}
function dirGet(_0) {
  return __async(this, arguments, function* (dir, path3 = getProjectPath()) {
    try {
      return yield readdir(path3 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + dir}`);
    }
  });
}
function dirDel(_0) {
  return __async(this, arguments, function* (dir, path3 = getProjectPath()) {
    try {
      yield rmdir(path3 + dir);
    } catch (error) {
      console.log(`Error: ${error}
Path: ${path3 + dir}`);
    }
  });
}

// src/openai.ts
import { promisify } from "util";
import { exec } from "child_process";
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
      const execPromise = promisify(exec);
      const { stdout, stderr } = yield execPromise(query);
      return JSON.parse(stdout).choices[0].message.content;
    });
  }
};

// src/octokit.ts
import { Octokit } from "@octokit/rest";
var ocotkit = class {
  constructor(token, owner, indent = 3, stringEncoding = "utf8", bufferEncoding = "base64") {
    // endpoints <
    this.urlFileGet = (repo, file) => `GET /repos/${this._owner}/${repo}/contents/${file}`;
    this.urlFilePut = (repo, file) => `PUT /repos/${this._owner}/${repo}/contents/${file}`;
    this._token = token;
    this._owner = owner;
    this._indent = indent;
    this._stringEncoding = stringEncoding;
    this._bufferEncoding = bufferEncoding;
    this._octokit = new Octokit({ auth: this._token });
  }
  // >
  request(_0) {
    return __async(this, arguments, function* (url, parameters = {}, property = "data", propertyElement = "") {
      let response = yield this._octokit.request(url, parameters);
      switch (propertyElement == "") {
        case true:
          return response[property];
        case false:
          return response[property].map((i) => i[propertyElement]);
      }
    });
  }
  repositoryGet(file, branch, repository, property = "content", suppressError = false) {
    return __async(this, null, function* () {
      let fileGet2 = this.urlFileGet(repository, file);
      try {
        let data = yield this.request(
          fileGet2,
          { ref: branch }
        );
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
export {
  dirDel,
  dirGet,
  dirSet,
  fileDel,
  fileGet,
  fileSet,
  getProjectPath,
  ocotkit,
  openai
};
