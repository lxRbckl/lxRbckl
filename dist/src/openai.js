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
const util_1 = require("util");
const child_process_1 = require("child_process");
// >
class openai {
    constructor(token, model = 'gpt-4o', temperature = 1.5) {
        this._model = model;
        this._token = token;
        this._temperature = temperature;
    }
    query(prompt) {
        return __awaiter(this, void 0, void 0, function* () {
            const query = `
      
         curl -X POST https://api.openai.com/v1/chat/completions \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${this._token}" \
            -d '{
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
            const execPromise = (0, util_1.promisify)(child_process_1.exec);
            const { stdout, stderr } = yield execPromise(query);
            return JSON.parse(stdout).choices[0].message.content;
        });
    }
}
// export <
module.exports = { openai };
// >
