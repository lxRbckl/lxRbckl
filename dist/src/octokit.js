"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
// import <
const rest_1 = require("@octokit/rest");
// >
class ocotkit {
    constructor(token, owner, indent = 3, stringEncoding = 'utf8', bufferEncoding = 'base64') {
        this.urlFileGet = (repo, file) => `GET /repos/${this._owner}/${repo}/contents/${file}`;
        this.urlFilePut = (repo, file) => `PUT /repos/${this._owner}/${repo}/contents/${file}`;
        this._token = token;
        this._owner = owner;
        this._indent = indent;
        this._stringEncoding = stringEncoding;
        this._bufferEncoding = bufferEncoding;
        this._octokit = new rest_1.Octokit({ auth: this._token });
    }
    repositoryGet(file_1, branch_1, repository_1) {
        return __awaiter(this, arguments, void 0, function* (file, branch, repository, property = 'content', suppressError = false) {
            // build url <
            let fileGet = this.urlFileGet(repository, file);
            // >
            // try (get) <
            // catch (then 403, 404) <
            try {
                let data = (yield this._octokit.request(fileGet, { ref: branch })).data;
                switch (property == 'content') {
                    case false: return data[property];
                    case true:
                        let encoding = data.encoding;
                        let buffer = Buffer.from(data.content, encoding);
                        return JSON.parse((buffer).toString(this._stringEncoding));
                }
            }
            catch (error) {
                suppressError ? console.log('Error: ', error, '\nQuery: ', fileGet, '\nBranch: ', branch) : undefined;
                return false;
            }
            // >
        });
    }
    respositorySet(data_1, file_1, branch_1, repository_1) {
        return __awaiter(this, arguments, void 0, function* (data, file, branch, repository, suppressError = false, message = 'Automated Action') {
            // build url <
            let filePut = this.urlFilePut(repository, file);
            // >
            // try (get) <
            // catch (then ) <
            try {
                yield this._octokit.request(filePut, {
                    branch: branch,
                    message: message,
                    owner: this._owner,
                    sha: yield this.repositoryGet(file, branch, repository, 'sha', suppressError),
                    content: Buffer.from(JSON.stringify(data, null, this._indent)).toString(this._bufferEncoding)
                });
                return true;
            }
            catch (error) {
                suppressError ? console.log('Error: ', error, '\nQuery: ', filePut, '\nBranch: ', branch) : undefined;
                return false;
            }
            // >
        });
    }
}
// export <
module.exports = { ocotkit };
// >
