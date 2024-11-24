// types <
export type OnReadyCallback = (...args: any[]) => Promise<void>;

export type InteractionCreateCallback = (...args: any[]) => Promise<void>;

// >


// interfaces <
interface Command {
   
   ctx?: Interaction,
   context(): commandBody;
   run: (...args: any[]) => any | Promise<any>;
   async registerChoices?: () => Promise<void>;

}


export interface Commands {

   [key: string]: Command

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