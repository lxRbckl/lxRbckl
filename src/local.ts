// import <
import path from 'path';
import {

   mkdir,
   rmdir,
   unlink,
   readdir,
   readFile,
   writeFile

} from 'fs/promises';

// >


function getProjectPath(
   
   file: string = '',
   delimeter: string = '/'

): string {
   
   const dir: string[] = path.dirname(__filename).split(/[]/);
   const base: number = (dir.includes('node_modules')) ? -4 : -1;

   return [...dir.slice(0, base), file.split(/[/\\]/)].join(delimeter);

}


async function fileSet(

   data: any,
   file: string,
   
   indent: number = 3,
   path: string = getProjectPath()

): Promise<void> {

   try {
      
      await writeFile(

         (path + file),
         file.endsWith('.json') ? JSON.stringify(data, null, indent) : data

      );

   } catch (error) {console.log(`Error: ${error}\nPath: ${path + file}`);}

}


async function fileGet(

   file: string,

   path: string = getProjectPath(),
   encoding: BufferEncoding = 'utf8'

): Promise<any> {

   try {

      const fin: Buffer | string = await readFile((path + file), encoding);
      return file.endsWith('.json') ? JSON.parse(fin.toString()) : fin;

   } catch (error) {console.log(`Error: ${error}\nPath: ${path + file}`);}

}


async function fileDel(

   file: string,
   path: string = getProjectPath()

): Promise<void> {

   try {await unlink(path + file);}
   catch (error) {console.log(`Error: ${error}\nPath: ${path + file}`);}

}


async function dirSet(

   dir: string,
   path: string = getProjectPath()

): Promise<void> {

   try {await mkdir(path + dir);}
   catch (error) {console.log(`Error: ${error}\nPath: ${path + dir}`);}

}


async function dirGet(

   dir: string,
   path: string = getProjectPath()

): Promise<any> {

   try {return await readdir(path + dir);}
   catch (error) {console.log(`Error: ${error}\nPath: ${path + dir}`);}

}


async function dirDel(

   dir: string,
   path: string = getProjectPath()

): Promise<void> {

   try {await rmdir(path + dir);}
   catch (error) {console.log(`Error: ${error}\nPath: ${path + dir}`)}

}


// export <
module.exports = {

   getProjectPath,
   fileSet,
   fileGet,
   fileDel,
   dirSet,
   dirGet,
   dirDel

};

// >