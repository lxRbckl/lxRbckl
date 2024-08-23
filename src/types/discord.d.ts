// types <
export type Commands = Command[];

export type onReadyCallback = (...args: any[]) => Promise<void>;

export type interactionCreateCallback = (...args: any[]) => Promise<void>;

// >


// interfaces <
interface Command {
   
   name?: string;

   context(): commandBody;
   run?: (...args: any[]) => any;
   async registerChoices?: () => Promise<void>;
   async run?: (...args: any[]) => Promise<any>;

}


export interface MappedCommands {

   [key: string]: Command;

}


export interface ConstructorParams {

   guildId: string;
   version?: string;
   channelId: string;
   intents?: number[];
   commands?: Commands;
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


interface bodyOptions {

   type: number;
   name: string;
   required: boolean;
   description: string;

}

interface commandBody {

   type?: number;
   name?: string;
   description?: string;
   options?: bodyOptions[];

}

// >