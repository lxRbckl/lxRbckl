// import <
const axios = require('axios');

// >


async function axiosGet(pURL) {

   try {

      const extension = pURL.split('.').slice(-1);
      const response = (await axios.get(pURL)).data;

      return {

         'txt' : () => {return response},
         'json' : () => {return JSON.parse(JSON.stringify(response))}

      }[extension]();
      
   } catch (error) {return 'Data could not be loaded.';}

}


// export <
module.exports = {

   axiosGet

};

// >