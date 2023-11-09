// < Project lxRbckl by Alex Arbuckle > //


// import <
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

   fileSet,
   fileGet,
   fileDel,
   axiosGet,
   githubSet,
   githubGet,
   githubUpdate

};

// >