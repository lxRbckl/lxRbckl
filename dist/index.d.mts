declare function getProjectPath(file?: string, delimeter?: string): string;
declare function fileSet(data: any, file: string, indent?: number, path?: string): Promise<void>;
declare function fileGet(file: string, path?: string, encoding?: BufferEncoding): Promise<any>;
declare function fileDel(file: string, path?: string): Promise<void>;
declare function dirSet(dir: string, path?: string): Promise<void>;
declare function dirGet(dir: string, path?: string): Promise<any>;
declare function dirDel(dir: string, path?: string): Promise<void>;

declare class openai {
    private readonly _model;
    private readonly _token;
    private readonly _temperature;
    constructor(token: string, model?: string, temperature?: number);
    query(prompt: string): Promise<string>;
}

declare class ocotkit {
    private _octokit;
    private readonly _token;
    private readonly _owner;
    private readonly _indent;
    private readonly _stringEncoding;
    private readonly _bufferEncoding;
    constructor(token: string, owner: string, indent?: number, stringEncoding?: BufferEncoding, bufferEncoding?: BufferEncoding);
    urlFileGet: (repo: string, file: string) => string;
    urlFilePut: (repo: string, file: string) => string;
    request(url: string, parameters?: any, property?: string, propertyElement?: string): Promise<any>;
    repositoryGet(file: string, branch: string, repository: string, property?: string, suppressError?: boolean): Promise<any>;
    respositorySet(data: object, file: string, branch: string, repository: string, suppressError?: boolean, message?: string): Promise<boolean>;
}

export { dirDel, dirGet, dirSet, fileDel, fileGet, fileSet, getProjectPath, ocotkit, openai };
