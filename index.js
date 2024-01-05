// < Project lxRbckl by Alex Arbuckle > //


// import <
const {gpt} = require('./source/gpt.js');
const {

   dirSet,
   dirGet,
   dirDel,
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

   gpt,
   
   dirSet,
   dirGet,
   dirDel,
   fileSet,
   fileGet,
   fileDel,
   axiosGet,
   githubSet,
   githubGet,
   githubUpdate

};

// >