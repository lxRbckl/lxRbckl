// import <
import { Octokit } from '@octokit/rest';
import {

   RepositoryGet,
   RepositorySet,
   EndpointFile,
   Constructor,
   Request

} from '../types/octokit';

// >


export class octokit {


   private _octokit: Octokit;

   private readonly _token: string;
   private readonly _owner: string;
   private readonly _indent: number;
   private readonly _stringEncoding: BufferEncoding;
   private readonly _bufferEncoding: BufferEncoding;


   constructor({
      
      token,
      owner,
      indent = 3,
      stringEncoding = 'utf8',
      bufferEncoding = 'base64'
   
   }: Constructor) {

      this._token = token;
      this._owner = owner;
      this._indent = indent;
      this._stringEncoding = stringEncoding;
      this._bufferEncoding = bufferEncoding;

      this._octokit = new Octokit({auth: this._token});

   }


   private endpointFile({

      file,
      method,
      repository

   }: EndpointFile): string {

      let endpoint: string = `${method} /repos/${this._owner}/${repository}/contents/${file}`;
      return endpoint;

   }


   public async request({

      endpoint,
      parameters = {},
      elementFromProperty = '',
      propertyFromResult = 'data'

   }: Request): Promise<any> {

      let response: any = await this._octokit.request(endpoint, parameters);

      switch (elementFromProperty == '') {

         case true: return response[propertyFromResult];
         case false: return response[propertyFromResult].map((i: any) => i[elementFromProperty]);

      }

   }


   public async repositoryGet({

      file,
      branch,
      repository,
      displayError = false,
      propertyFromResult = 'content'

   }: RepositoryGet): Promise<any> {
      
      let endpoint: string = this.endpointFile({

         file : file,
         method : 'GET',
         repository : repository

      });

      // try (get) <
      // catch (then 403, 404) <
      try {

         let data: any = await this.request({

            endpoint: endpoint,
            parameters : {ref : branch}

         });

         switch (propertyFromResult == 'content') {

            case false: return data[propertyFromResult];
            case true: 

               let encoding: BufferEncoding = data.encoding;
               let buffer: Buffer = Buffer.from(data.content, encoding);

               return JSON.parse((buffer).toString(this._stringEncoding));

         }

      } catch (error) {

         displayError ? console.log('Error: ', error) : undefined;
         return false;
   
      }

      // >
      
   }


   public async respositorySet({

      data,
      file,
      branch,
      repository,
      isMarkdown = false,
      displayError = false,
      commitMessage = 'Automated Action'

   }: RepositorySet): Promise<boolean> {

      data = isMarkdown ? data : JSON.stringify(data, null, this._indent);
      let endpoint: string = this.endpointFile({

         file : file,
         method: 'PUT',
         repository: repository

      });

      // try (get) <
      // catch (then ) <
      try {

         await this._octokit.request(endpoint, {

            branch : branch,
            owner : this._owner,
            message : commitMessage,
            content : Buffer.from(data as string).toString(this._bufferEncoding),
            sha : await this.repositoryGet({

               file : file,
               branch : branch,
               repository : repository,
               propertyFromResult : 'sha',
               displayError : displayError

            })

         });

         return true;

      } catch (error) {

         displayError ? console.log('Error: ', error) : undefined;
         return false;

      }

      // >

   }


}