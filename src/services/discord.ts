// import <
import {
   
   Client,
   Routes,
   Channel,
   TextChannel,
   IntentsBitField

} from 'discord.js';

import {

   command,
   onReadyCallback,
   interactionCreateCallback

} from '../types/discord';

// >


 export class discord {


   private _client: Client;
   private _version: string;
   private _guildId: string;
   private _intents: number[];
   private _channelId: string;
   private _applicationId: string;


   constructor(

      guildId: string,
      channelId: string,
      applicationId: string,

      version: string = '10',
      intents: number[] = [

         IntentsBitField.Flags.Guilds,
         IntentsBitField.Flags.GuildMembers,
         IntentsBitField.Flags.GuildMessages,
         IntentsBitField.Flags.MessageContent

      ]

   ) {

      this._version = version;
      this._intents = intents;
      this._guildId = guildId;
      this._channelId = channelId;
      this._applicationId = applicationId;

      this._client = new Client({

         intents : this._intents,
         rest : {version : this._version}

      });

   }


   login(token: string): void {this._client.login(token);}


   messageChannel(
      
      content: string, 
      isInline: boolean = false,
      isSpoiler: boolean = false
   
   ): void {

      try {

         let channel: Channel = this._client.channels.cache.get(this._channelId)!;

         if (channel instanceof TextChannel) {

            content = isInline ? `\` ${content} \`` : content;
            content = isSpoiler ? `|| ${content} ||` : content;

            channel.send(content);

         }
         
         
      } catch (error) {

         console.log('Error: ', error, '\nChannelId: ', this._channelId);

      }

   }   
 
   
   registerCommands(commands: any): void {

      this._client.rest.put(

         Routes.applicationGuildCommands(

            this._applicationId,
            this._guildId

         ),
         {body : commands.map((c: command) => c.context())}

      )
      
   }


   async registerOnReady(callback: onReadyCallback): Promise<void> {

      this._client.on('ready', async (): Promise<void> => {

         await callback();

      });

   }


   async registerInteractionCreate(callback: interactionCreateCallback): Promise<void> {

      this._client.on('interactionCreate', async (interaction): Promise<void> => {

         await callback(interaction);

      });

   }

}