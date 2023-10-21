// < Project lxRbckl by Alex Arbuckle > //


// import <
const {

   fileSet,
   fileGet,
   fileDel

} = require('./source/local.js');
const {

   axiosGet

} = require('./source/remote.js');

// >


// export <
module.exports = {

   fileSet,
   fileGet,
   fileDel,
   axiosGet

};

// >