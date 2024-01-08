// import <
const {OpenAI} = require('openai');

// >


class gpt {

   constructor({
      
      token,
      role = 'user',
      model = 'gpt-3.5-turbo'
   
   }) {

      this.role = role;
      this.model = model;
      this.openai = new OpenAI({apiKey : token});

   }


   async message({query}) {

      return (await this.openai.chat.completions.create({

         model : this.model,
         messages : [{

            content : query,
            role : this.role

         }]

      })).choices[0].message.content;

   }

}


// export <
module.exports = gpt;

// >