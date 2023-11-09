// import <
const axios = require('axios');

// >


async function axiosGet({
   
   pURL,
   pErrorMessage = 'Data could not be loaded.'

}) {

   try { return (await axios.get(pURL)).data}   
   catch (error) {return pErrorMessage;}

}


// export <
module.exports = {

   axiosGet,
   githubGet,
   githubUpdate

};

// >