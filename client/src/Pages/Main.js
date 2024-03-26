import './Main.css';
import styled from "styled-components";
import { useNavigate } from "react-router-dom";

function Main() {
    const Title = styled.h1`
        font-size:70px;
        font-weight: bold;         
    `
    const Main = styled.div`
        display:flex;
        align-items: center;
        width: 100vw;
        height: 100vh;
        flex-direction: column; 
    `;
    const Example = styled.div`
        display:flex;
        justify-content: center;
        align-items: center;
    `;
    const ExImg = styled.img`
        margin: 0 40px ;
    `
    const ImgDiv = styled.div`
        flex-direction: column;
        `
    const Step = styled.p`
        text-align:center;
    `
    const Btn = styled.button`
        width:442px;
        height:89px;
        border-radius: 90px; 
        background-color:white;
        color:black;
        font-size:30px;
        font-weight: bold;
        position: relative;
        border: none;
        cursor: pointer;
        box-shadow: 6px 6px 6px rgba(255, 255, 255, 0.64);
        font-weight: 700;
        transition: 0.3s;
    
    &:hover {
        transform: scale(1.2);
    }
    `;
    const navigate = useNavigate();
 
    const navigateToFile = () => {
        navigate("/file");
    };
    
    return (
        <Main>
        <Title>이름표 제작 메커니즘</Title>
        <Example>
            <ImgDiv>
                <ExImg src='../../excel_example.png' width='514px' height='479px'></ExImg>
                <Step>step1</Step>
            </ImgDiv>
            <ExImg src='../../arrow.png' width='86px' height='86px'></ExImg>
            <ImgDiv>
                <ExImg src='../../ppt_example.png' width='354px' height='479px'></ExImg>
                <Step>step2</Step>                
            </ImgDiv>
        </Example>        
        <Btn onClick={navigateToFile}>이름표 만들기로 넘어가기</Btn>
    </Main>
  );
}

export default Main;
