export function Main({ title = "The main event", content = "Happens here" }) {
    return (
        <>
            <h1>{title}</h1>
            <p>{content}</p>
        </>
    );
}