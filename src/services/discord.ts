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
   LoginParams,
   MessageChannel,
   onReadyCallback,
   RegisterCommands,
   ConstructorParams,
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


   constructor({

      guildId,
      channelId,
      applicationId,

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
      this._channelId = channelId;
      this._applicationId = applicationId;

      this._client = new Client({intents : this._intents, rest : {version : this._version}});
      

   }


   // required
   public login({token}: LoginParams): void {this._client.login(token);}
 
   
   // required
   public registerCommands({commands}: RegisterCommands): void {

      this._client.rest.put(

         Routes.applicationGuildCommands(

            this._applicationId,
            this._guildId

         ),
         {body : commands.map((c: command) => c.context())}

      );
      
   }


   // optional
   public terminate(): void {this._client.destroy();}


   // optional
   public async registerOnReady(callback: onReadyCallback): Promise<void> {

      this._client.on('ready', async (): Promise<void> => {

         await callback();

      });

   }


   // optional
   public async registerInteractionCreate(callback: interactionCreateCallback): Promise<void> {

      this._client.on('interactionCreate', async (interaction): Promise<void> => {

         await callback(interaction);

      });

   }


   // optional
   public messageChannel({

      content,
      codeBlock = '',
      isInline = false,
      isSpoiler = false

   }: MessageChannel): void {

      try {

         let channel: Channel = this._client.channels.cache.get(this._channelId)!;

         if (channel instanceof TextChannel) {

            content = isInline ? `\` ${content} \`` : content;
            content = isSpoiler ? `|| ${content} ||` : content;
            content = codeBlock ? `\`\`\`${codeBlock}\n${content}\`\`\`` : content;

            channel.send(content);

         }
         
      } catch (error) {console.log('Error: ', error, '\nChannelId: ', this._channelId);}

   }

}