import styled from 'styled-components';

export const Title = styled.h1`
font-size:70px;
font-weight: bold;         
`
export const Main = styled.div`
display:flex;
align-items: center;
width: 100vw;
height: 100vh;
flex-direction: column; 
`;
export const Example = styled.div`
display:flex;
justify-content: center;
align-items: center;
`;
export const ExImg = styled.img`
margin: 0 40px ;
`
export const ImgDiv = styled.div`
flex-direction: column;
`
export const Step = styled.p`
text-align:center;
`
export const Btn = styled.button`
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