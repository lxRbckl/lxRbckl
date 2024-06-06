// import <

import { promisify } from 'util';
import { exec } from 'child_process';

// >


class openai {


   private readonly _model: string;
   private readonly _token: string;
   private readonly _temperature: number;
   

   constructor(

      token: string,

      model: string = 'gpt-4o',
      temperature: number = 1.5

   ) {

      this._model = model;
      this._token = token;
      this._temperature = temperature;
      
   }


   async query(prompt: string): Promise<string> {

      const query: string = `
      
         curl -X POST https://api.openai.com/v1/chat/completions \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${this._token}" \
            -d '{
                  "model" : "${this._model}",
                  "temperature" : ${this._temperature},
                  "messages" : [
                     {
                        "role" : "system",
                        "content" : "You are a helpful assistant."
                     },
                     {
                        "role" : "user",
                        "content" : "${prompt}"
                     }
                  ]
               }'
      
      `;

      const execPromise = promisify(exec);
      const {stdout, stderr} = await execPromise(query);

      return JSON.parse(stdout).choices[0].message.content;

   }

}


// export <
module.exports = {openai};

// >