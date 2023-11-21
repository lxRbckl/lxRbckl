// < Project lxRbckl by Alex Arbuckle > //


// import <
const {chatgpt} = require('./source/chatgpt.js');
const {

   fileSet,
   fileGet,
   fileDel

} = require('./source/local.js');
const {

   axiosGet,
   githubGet,
   githubSet,
   githubUpdate

} = require('./source/remote.js');

// >


// export <
module.exports = {

   chatgpt,
   fileSet,
   fileGet,
   fileDel,
   axiosGet,
   githubSet,
   githubGet,
   githubUpdate

};

// >