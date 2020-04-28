import React, { FunctionComponent, useState, useEffect, Component } from 'react';
import { StyledText, StyledInput } from '../style';
import axios from "axios";
import { url as _url } from '../../url';

const DailyInput: FunctionComponent<any> = ({ }) => {
  var date = new Date(); 
  var year = date.getFullYear(); 
  var month = new String(date.getMonth()+1); 
  var day = new String(date.getDate());
  
  // 한자리수일 경우 0을 채워준다. 
  if(month.length == 1){ 
    month = "0" + month; 
  } 
  if(day.length == 1){ 
    day = "0" + day; 
  } 
  
  // const changeDate = () => {
  //   // const breakfast_id = e.target.id;
  //   setDate(year + "-" + month + "-" + day)
  // }

  const [breakfast, setBreakfast] = useState(0);
  const changeBreakfast = (e: any) => {
    // const breakfast_id = e.target.id;
    const breakfast_value = parseInt(e.target.value);
    setBreakfast(breakfast_value)
  }

  const [lunch, setLunch] = useState(0);
  const changeLunch = (e: any) => {
    // const lunch_id = e.target.id;
    const lunch_value = parseInt(e.target.value);
    setLunch(lunch_value);
  }


  const [dinner, setDinner] = useState(0);
  const changeDinner = (e: any) => {
    // const dinner_id = e.target.id;
    const dinner_value = parseInt(e.target.value);
    setDinner(dinner_value);
  }

  const [total, setTotal] = useState(0);
  const changeTotal = () => {
    // const breakfast_id = e.target.id;
    const total_value = breakfast + lunch + dinner
    setTotal(total_value)
  }

  const onSubmit = async () => {
    var flag = 0;
    var e_id = 0;
    try {
      const _id = window.sessionStorage.getItem('id')
      const response = await axios({
        method: "get",
        url: `${_url}/api/user_detail/${_id}/`,
        responseType: "json"
      });
      response.data.history.forEach(element => {
        if (element.payment_date === year + "-" + month + "-" + day) {
          e_id = element.id
          flag = 1;
        }  
      })
      if (flag === 1) {
          await axios({
            method: "put",
            url: `${_url}/api/history_detail/${e_id}/`,
            data: {
              kakao: _id,
              user_breakfast: breakfast,
              user_lunch: lunch,
              user_dinner: dinner,
            },
            responseType: "json"
          });
      } else {
          const res = await axios({
            method: "post",
            url: `${_url}/api/history_list/`,
            data: {
              kakao: _id,
              payment_date: date,
              user_breakfast: breakfast,
              user_lunch: lunch,
              user_dinner: dinner,
            },
            
            responseType: "json"
          });
        }
    } catch (err) {
      alert(err); // WTF?
    }
  }
  // const selectNum = () => {
  //   var numSelect = document.getElementById("price");
  //   if (numSelect) {
  //     console.log(numSelect)
  //     // var text = numSelect.options[document.getElementById("price").selectedIndex].text;

  //     // // // option value 가져오기
  //     // document.getElementById('price').value = this.options[this.selectedIndex].value
      
  //     // var value = numSelect.options[document.getElementById("price").selectedIndex].value
  //   }
  //   // text 가져오기
    
    
  //   }
  return (
    <>
      <StyledText>
        <h3>나는 오늘 아침에 <StyledInput onChange={changeBreakfast} />
        점심에 <StyledInput onChange={changeLunch} />
        저녁에 <StyledInput onChange={changeDinner} />
          원 썼어요</h3>
          <button onClick={onSubmit}>추가</button>
        <h2>총 합: {breakfast+lunch+dinner}</h2>
      </StyledText>
    </>
  )
}

export default DailyInput;