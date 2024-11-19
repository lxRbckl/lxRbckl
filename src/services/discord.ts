// import <
import {
   
   Client,
   Routes,
   Channel,
   TextChannel,
   IntentsBitField

} from 'discord.js';

import {

   Commands,
   LoginParams,
   MessageChannel,
   OnReadyCallback,
   ConstructorParams,
   InteractionCreateCallback

} from '../types/discord';

// >


 export class discord {


   private _client: Client;
   private _version: string;
   private _guildId: string;
   public commands: Commands;
   private _intents: number[];
   private _channelId: string;
   private _applicationId: string;


   constructor({

      guildId,
      channelId,
      applicationId,

      commands = {},
      version = '10',
      intents = [

         IntentsBitField.Flags.Guilds,
         IntentsBitField.Flags.GuildMembers,
         IntentsBitField.Flags.GuildMessages,
         IntentsBitField.Flags.MessageContent

      ]

   }: ConstructorParams) {

      this._version = version;
      this._intents = intents;
      this._guildId = guildId;
      this.commands = commands;
      this._channelId = channelId;
      this._applicationId = applicationId;

      this._client = new Client({intents : this._intents, rest : {version : this._version}});
      

   }


   // required //
   public login({token}: LoginParams): void {this._client.login(token);}
 
   
   // required //
   public registerCommands(): void {

      this._client.rest.put(

         Routes.applicationGuildCommands(

            this._applicationId,
            this._guildId

         ),
         {body : Object.values(this.commands).map(c => c.context())}

      );
      
   }


   // suggested //
   public async registerOnReady(callback: OnReadyCallback): Promise<void> {

      this._client.on('ready', async (): Promise<void> => {

         await callback();

      });

   }


   // suggested //
   public async registerInteractionCreate(callback: InteractionCreateCallback): Promise<void> {

      this._client.on('interactionCreate', async (interaction): Promise<void> => {

         await callback(interaction);

      });

   }


   // optional //
   public async registerCommandChoices() {

      // register all choices concurrently <
      await Promise.all(

         Object.values(this.commands)

           .filter((c) => c.registerChoices)
           .map((c) => c.registerChoices!())

       );

       // >

   }


   // optional //
   public messageChannel({

      content,
      codeBlock = '',
      isInline = false,
      isSpoiler = false

   }: MessageChannel): void {

      try {

         // if (message) <
         // else (then no message) <
         if (content.length > 0) {

            let channel: Channel = this._client.channels.cache.get(this._channelId)!;

            if (channel instanceof TextChannel) {

               content = isInline ? `\` ${content} \`` : content;
               content = isSpoiler ? `|| ${content} ||` : content;
               content = codeBlock ? `\`\`\`${codeBlock}\n${content}\`\`\`` : content;

               channel.send(content);

            }

         } else {console.log('There is no content.');}

         // >
         
      } catch (error) {console.log('Error: ', error, '\nChannelId: ', this._channelId);}

   }


   // optional //
   public terminate(): void {this._client.destroy();}


}