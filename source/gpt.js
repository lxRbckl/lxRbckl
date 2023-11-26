// import <
const {OpenAI} = require('openai');

// >


class chatgpt {

   constructor(token) {

      this.openai = new OpenAI({apiKey : token});

   }


   async message(

      content,
      role = 'user',
      model = 'gpt-3.5-turbo'

   ) {


      const response = await this.openai.chat.completions.create({

         model : model,
         messages : [{

            role : role,
            content : content

         }]

      });
      return response.choices[0].message.content;

   }

}


// export <
module.exports = {chatgpt};

// >