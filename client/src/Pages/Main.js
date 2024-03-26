import './Main.style.js';
import * as S from './Main.style';
import { useNavigate } from "react-router-dom";

function Main() {
   
    const navigate = useNavigate();
 
    const navigateToFile = () => {
        navigate("/file");
    };

    return (
        <S.Main>
        <S.Title>이름표 제작 메커니즘</S.Title>
        <S.Example>
            <S.ImgDiv>
                <S.ExImg src='../../excel_example.png' width='514px' height='479px'></S.ExImg>
                <S.Step>step1</S.Step>
            </S.ImgDiv>
            <S.ExImg src='../../arrow.png' width='86px' height='86px'></S.ExImg>
            <S.ImgDiv>
                <S.ExImg src='../../ppt_example.png' width='354px' height='479px'></S.ExImg>
                <S.Step>step2</S.Step>                
            </S.ImgDiv>
        </S.Example>        
        <S.Btn onClick={navigateToFile}>이름표 만들기로 넘어가기</S.Btn>
    </S.Main>
  );
}

export default Main;
