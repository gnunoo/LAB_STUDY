import styled from "styled-components";
import type {FC} from "react" 
import { MovieInfo } from "../types/MovieInfo";
const IMG_BASE_URL ="https://image.tmdb.org/t/p/w1280/";
export const Movie: FC<MovieInfo.Result>=props =>{
    const {title,poster_path,vote_average}=props;
    return(
        <>
            <SmovieContaniner>
                <SmovieImg src={IMG_BASE_URL+poster_path} alt="영화포스터" />
                <SmovieInfo>
                    <Sh4>{title}</Sh4>
                    <Sspan>{vote_average}</Sspan>
                </SmovieInfo>
            </SmovieContaniner>
        </>
       
    )

};
const SmovieContaniner=styled.div`
    width:250px;
    margin:16px;
    background-color #373b69:
    color: white;
    border-radius: 5px;
    box-shadow: 3px 3px 5px rgba(0,0,0,0.1);
    border: 1px solid red;

`;
const SmovieImg=styled.img`
    max-width: 100%;
`;
const SmovieInfo=styled.div`
   display:flex;
   padding:20px;
   justfy-content:space-between;
   align-items: center;

`;
const Sh4=styled.h4`
    margin: 0;
`;
const Sspan=styled.span`
    margin-left: 10px;
`;