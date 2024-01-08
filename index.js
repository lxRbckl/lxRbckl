// < Project lxRbckl by Alex Arbuckle > //


// import <
const gpt = require('./source/fp/gpt.js');
const local = require('./source/oop/local.js');
const {

   dirSet,
   dirGet,
   dirDel,
   fileSet,
   fileGet,
   fileDel

} = require('./source/fp/local.js');
const {

   axiosGet,
   githubGet,
   githubSet,
   githubUpdate

} = require('./source/fp/remote.js');

// >


// export <
module.exports = {

   gpt,
   local,
   
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