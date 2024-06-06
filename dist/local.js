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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// import <
const path_1 = __importDefault(require("path"));
const promises_1 = require("fs/promises");
// >
function getProjectPath(file = '', delimeter = '/') {
    const dir = path_1.default.dirname(__filename).split(/[]/);
    const base = (dir.includes('node_modules')) ? -4 : -1;
    return [...dir.slice(0, base), file.split(/[/\\]/)].join(delimeter);
}
function fileSet(data_1, file_1) {
    return __awaiter(this, arguments, void 0, function* (data, file, indent = 3, path = getProjectPath()) {
        try {
            yield (0, promises_1.writeFile)((path + file), file.endsWith('.json') ? JSON.stringify(data, null, indent) : data);
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + file}`);
        }
    });
}
function fileGet(file_1) {
    return __awaiter(this, arguments, void 0, function* (file, path = getProjectPath(), encoding = 'utf8') {
        try {
            const fin = yield (0, promises_1.readFile)((path + file), encoding);
            return file.endsWith('.json') ? JSON.parse(fin.toString()) : fin;
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + file}`);
        }
    });
}
function fileDel(file_1) {
    return __awaiter(this, arguments, void 0, function* (file, path = getProjectPath()) {
        try {
            yield (0, promises_1.unlink)(path + file);
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + file}`);
        }
    });
}
function dirSet(dir_1) {
    return __awaiter(this, arguments, void 0, function* (dir, path = getProjectPath()) {
        try {
            yield (0, promises_1.mkdir)(path + dir);
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + dir}`);
        }
    });
}
function dirGet(dir_1) {
    return __awaiter(this, arguments, void 0, function* (dir, path = getProjectPath()) {
        try {
            return yield (0, promises_1.readdir)(path + dir);
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + dir}`);
        }
    });
}
function dirDel(dir_1) {
    return __awaiter(this, arguments, void 0, function* (dir, path = getProjectPath()) {
        try {
            yield (0, promises_1.rmdir)(path + dir);
        }
        catch (error) {
            console.log(`Error: ${error}\nPath: ${path + dir}`);
        }
    });
}
// export <
module.exports = {
    getProjectPath,
    fileSet,
    fileGet,
    fileDel,
    dirSet,
    dirGet,
    dirDel
};
// >
