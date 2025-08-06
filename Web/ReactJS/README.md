# React

## simple

This project is the old React method of creating an application with;

```sh
npm create-react-app simple
```

This has now been deprecated.

## new-simple

This is created using the newer method and [vite](https://vite.dev/guide/).

```sh
npm create vite@latest new-simple -- --template react
```

A key point to notice is the naming of the file extensions to **jsx** for regular JavaScript and **tsx** if you use **react-ts** when invoking the project - which is TypeScript.

Another point is the starting files, with **index.html** which calls the components in the **src** directory, starting with **main.jsx**.  The **main.jsx** in turn is similar to the original **index.js** in the older method.

To run the Vite project;

```
npx vite
```

The actions are still in the package.json file.