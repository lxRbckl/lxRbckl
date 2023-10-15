// import <
const assert = require('assert');
const {axiosGet} = require('../source/remote.js');

// >


// declare <
const gValidLink = 'https://raw.githubusercontent.com/lxRbckl/Project-Domum/main/Domum.json';
const gInvalidLink = 'https://raw.githubusercontent.com/lxRbckl/lxRbckl/python/test/invalid.json';

// >


describe('axiosGet() Test Suite', async () => {

   it('can load valid links', async () => {

      const expected = {};
      const result = await axiosGet({pURL : gValidLink});
      assert.deepEqual(result, expected);

   });
   it('can detect invalid links', async () => {

      const expected = 'Data could not be loaded.';
      const result = await axiosGet({pURL : gInvalidLink});
      assert.strictEqual(result, expected);

   });

});