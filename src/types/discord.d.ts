// types <
export type onReadyCallback = (...args: any[]) => Promise<void>;

export type interactionCreateCallback = (...args: any[]) => Promise<void>;

// >


// interfaces <
export interface ConstructorParams {

   guildId: string;
   version?: string;
   channelId: string;
   intents?: number[];
   applicationId: string;

}


export interface LoginParams {

   token: string;

}


export interface MessageChannel {

   content: string;
   isInline?: boolean;
   codeBlock?: string;
   isSpoiler?: boolean;

}


export interface RegisterCommands {

   commands: any;

}


interface bodyOptions {

   type: number;
   name: string;
   required: boolean;
   description: string;

}

interface commandBody {

   type: number;
   name: string;
   description: string;
   options: bodyOptions[];

}

export interface command {
   
   context(): commandBody

}

// >