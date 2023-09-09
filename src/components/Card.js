import "./Card.css";

//import all car logos
import Ferrari from "../images/ferrari.png";
import Ford from "../images/ford.png";
import NoImage from "../images/NoImage.png";



//import testing image
import Testa from "../images/testa_rossa.jpeg";

export default function Card  ({make, model, generation, rarity}) 
{
    var styles = make;
    var logo = NoImage;
    function setupStyles(make, rarity)
    {
        if (rarity > 10)
        {
            styles += " textured";
        }
        if (rarity > 20)
        {
            styles += " animatedName";
        }

        switch(make)
        {
            case "Ferrari":
                logo = Ferrari;
                break;

            case "Ford":
                logo = Ford;
                break;
                
            default:
                logo = NoImage;
                break;
        }
    }

    setupStyles(make, rarity);


    return (

        <div className= {styles}>
            <div className="card">
                <div className="cardHeader">
                    <img src={logo} className="logo"/>
                    <div class="cardHeader">
                        <p class="title">{make} {model}</p>
                        <p class="title cover">{make} {model}</p>
                    </div>

                </div>
                <div>
                    <img className="cardImage" src={Testa}/>
                </div>
                
            </div>
        </div>
    );
};