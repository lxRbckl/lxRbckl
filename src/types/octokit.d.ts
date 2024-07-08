// types <


// >


// interfaces <
export interface Constructor {

   token: string;
   owner: string;
   indent?: number;
   stringEncoding?: BufferEncoding;
   bufferEncoding?: BufferEncoding;

}


export interface EndpointFile {

   file: string;
   repository: string;
   method: 'GET' | 'PUT';

}


export interface Request {

   endpoint: string;
   parameters?: any;
   propertyFromResult?: string;
   elementFromProperty?: string;

}


export interface RepositoryGet {

   file: string;
   branch: string;
   repository: string;
   displayError?: boolean;
   propertyFromResult?: string;

}


export interface RepositorySet {

   file: string;
   branch: string;
   repository: string;
   data: string | object;
   displayError?: boolean;
   commitMessage?: string;

}

// >