import { useEffect, useState, useMemo } from 'react';

interface Article {
    title: string;
    content: string;
}

const initialArticles: Article[] = [
    { title: 'ONE', content: '' },
    { title: 'TWO', content: '' },
    { title: 'THREE', content: '' }
];

export default function useArticles() {
    const [articles, setArticles] = useState(initialArticles);

    const getArticles = () => {
        fetch('articles.json')
            .then(r => r.json())
            .then(data => setArticles(data));
    };

    useEffect(() => { getArticles() }, []);

    const repository = useMemo(() => ({
        list() {
            return articles;
        },
        count() {
            return articles.length;
        },
        isValidId(id: number) {
            return id >= 0 && id < articles.length;
        },
        byId(id: number) {
            return this.isValidId(id) ? articles[id] : null;
        },
        add(title: string, content: string) {
            setArticles(prev => [...prev, { title, content }]);
        },
        delete(id: number) {
            setArticles(prev => prev.filter((_, i) => i !== id));
        }
    }), [articles]);

    return repository;
}
