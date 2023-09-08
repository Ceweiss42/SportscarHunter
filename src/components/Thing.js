import "./Thing.css";

export default function Thing  ({name, number}) 
{
    return (
        <div>
            <h1>Hello, my name is <name>{name}</name>!</h1>
            <h2> My favorite number is <number>{number}</number>. Nice to meet you!</h2>
        </div>
    );
};