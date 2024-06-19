// import <
import { Octokit } from '@octokit/rest';

// >


export class octokit {


   private _octokit: Octokit;

   private readonly _token: string;
   private readonly _owner: string;
   private readonly _indent: number;
   private readonly _stringEncoding: BufferEncoding;
   private readonly _bufferEncoding: BufferEncoding;


   constructor(
      
      token: string,
      owner: string,
      indent: number = 3,
      stringEncoding: BufferEncoding = 'utf8',
      bufferEncoding: BufferEncoding = 'base64'
   
   ) {

      this._token = token;
      this._owner = owner;
      this._indent = indent;
      this._stringEncoding = stringEncoding;
      this._bufferEncoding = bufferEncoding;

      this._octokit = new Octokit({auth: this._token});

   }


   // endpoints <
   urlFileGet = (repo: string, file: string): string => `GET /repos/${this._owner}/${repo}/contents/${file}`;
   urlFilePut = (repo: string, file: string): string => `PUT /repos/${this._owner}/${repo}/contents/${file}`;

   // >


   public async request(

      url: string,
      parameters: any = {},
      property: string = 'data',
      propertyElement: string = ''

   ): Promise<any> {

      let response: any = await this._octokit.request(url, parameters);

      switch (propertyElement == '') {

         case true: return response[property];
         case false: return response[property].map((i: any) => i[propertyElement]);

      }

   }


   public async repositoryGet(

      file: string,
      branch: string,
      repository: string,

      property: string = 'content',
      suppressError: boolean = false

   ): Promise<any> {
      
      // build url <
      let fileGet: string = this.urlFileGet(repository, file);

      // >

      // try (get) <
      // catch (then 403, 404) <
      try {

         let data: any = await this.request(

            fileGet,
            {ref : branch}

         );

         switch (property == 'content') {

            case false: return data[property];
            case true: 

               let encoding: BufferEncoding = data.encoding;
               let buffer: Buffer = Buffer.from(data.content, encoding);

               return JSON.parse((buffer).toString(this._stringEncoding));

         }

      } catch (error) {

         suppressError ? console.log('Error: ', error, '\nQuery: ', fileGet, '\nBranch: ', branch) : undefined;
         return false;
   
      }

      // >
      
   }


   public async respositorySet(

      file: string,
      branch: string,
      repository: string,
      data: string | object,

      isMarkdown: boolean = false,
      suppressError: boolean = false,
      message: string = 'Automated Action'

   ): Promise<boolean> {

      // build url <
      let filePut: string = this.urlFilePut(repository, file);
      data = isMarkdown ? data : JSON.stringify(data, null, this._indent);

      // >

      // try (get) <
      // catch (then ) <
      try {

         await this._octokit.request(filePut, {

            branch : branch,
            message : message,
            owner : this._owner,
            content : Buffer.from(data as string).toString(this._bufferEncoding),
            sha : await this.repositoryGet(file, branch, repository, 'sha', suppressError)

         });

         return true;

      } catch (error) {

         suppressError ? console.log('Error: ', error, '\nQuery: ', filePut, '\nBranch: ', branch) : undefined;
         return false;

      }

      // >

   }


}