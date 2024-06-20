// types <
export type onReadyCallback = (...args: any[]) => Promise<void>;


export type interactionCreateCallback = (...args: any[]) => Promise<void>;


type bodyOptions = {

   type: number,
   name: string,
   required: boolean,
   description: string

};
type commandBody = {

   type: number,
   name: string,
   description: string,
   options: bodyOptions[]

};

// >


// interfaces <
export interface command {context(): commandBody;}

// >