
import { useEffect, useState } from 'react';

interface Article {
    title: string;
    content: string;
}

const initialArticles: Article[] = [
    { title: 'ONE', content: '' },
    { title: 'TWO', content: '' },
    { title: 'THREE', content: '' }
];

function useArticles() {
    const [articles, setArticles] = useState(initialArticles);

    const getArticles = function () {
        fetch('articles.json')
            .then(response => response.json())
            .then(data => {
                setArticles(data)
            });
    }

    useEffect(() => { getArticles() }, []);

    const repository = {
        list() {
            return articles;
        },
        count() {
            return articles.length;
        },
        isValidId(id:number) {
            return id >= 0 && id < articles.length;
        },
        byId(id:number) {
            if (this.isValidId(id)) {
                return articles[id];
            } else {
                return null;
            }
        },
        add(title:string, content:string) {
            setArticles([...articles, { title, content }]);
        },
        delete(id:number) {
            articles.splice(id, 1);
            setArticles([...articles]);
        },
    };

    return repository;
}

export type { Article };
export default useArticles;