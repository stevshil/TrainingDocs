import './App.css';
import { useState } from 'react';
import useArticles from './repository';
import type { Article } from './repository';

const initialFormObject: Article = { title: 'title1', content: 'content1' };

export default function App() {
    const articles: any = useArticles();

    const [formObject, setFormObject] = useState(initialFormObject);
    const [selectedArticleId, setSelectedArticleId] = useState(-1);
    const selectedArticle = articles.byId(selectedArticleId)?.content || 'none';
    const changeHandler = function (event: any) {
        
        const name = event.target.name;
        const value = event.target.value;
        // const { name, value } = event.target;  // Shorter way of writing the 2 lines above

        // Offending code - overwrites every time and is not using the correct name and values for the text boxes.
        // let currentFormObject: Article = { 'title': name, 'content': value }
        // Keeps reseting the form
        // setFormObject({ ...currentFormObject })

        // The correct code
        setFormObject(prev => ({ ...prev, [name]: value }));
        // The original code didn't include the whole form
        // The original code was not using the correct title and content for the input box
    }
    return (
        <div className={'app'}>
            <h2>React Custom Hooks App</h2>
            <ul>
                {articles.list().map(
                    (article: Article, index: number) => {
                        return <li key={index}
                            className={
                                (selectedArticleId == index) ? 'selected' : ''
                            }
                            onClick={(event) => setSelectedArticleId(index)}>
                            {article.title}</li>
                    }
                )}
            </ul>
            <br /><span className={'bold'}>Selected Article:</span>
            <p>{selectedArticle}</p><br />
            <br />
            <div className={'controls'}>
                <span className={'bold'}>Controls:</span><br />
                <button 
                    onClick={() => { articles.add(formObject.title, formObject.content);
                        setFormObject(initialFormObject);
                    }}
                >Add</button>
                <button 
                    onClick={() => articles.delete(selectedArticleId)}
                    disabled={!articles.isValidId(selectedArticleId)}
                >Delete</button>
                <br />
                <input type={'text'} name={'title'}
                    placeholder={'title'} value={formObject.title}
                    onChange={(e) => changeHandler(e)}
                /><br />
                <input type={'text'} name={'content'}
                    placeholder={'content'} value={formObject.content}
                    onChange={(e) => changeHandler(e)}
                /><br />
            </div>
        </div >

    );
}