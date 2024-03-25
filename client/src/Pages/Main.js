import './Main.css';
import styled from "styled-components";


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
    const Btn = styled.button`
        width:442px;
        height:89px;
        border-radius: 90px; 
        margin-top:60px;
        background-color:white;
        color:black;
        font-size:30px;
        font-weight: bold;
        `


  return (
    <Main>
        <Title>이름표 제작 메커니즘</Title>
        <Example>
            <ExImg src='../../excel_example.png' width='514px' height='479px'></ExImg>
            <ExImg src='../../arrow.png' width='86px' height='86px'></ExImg>
            <ExImg src='../../ppt_example.png' width='354px' height='479px'></ExImg>
        </Example>        
        <Btn>이름표 만들기로 넘어가기</Btn>
    </Main>
  );
}

export default Main;
