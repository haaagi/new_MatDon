import React from "react";
import ReactFullpage from "@fullpage/react-fullpage";
import Greeting from "./components/Pages/00Greeting";
import Service from "./components/Pages/01Service";
import MonthlyInput from "./components/Pages/05MonthlyInput";
import DailyInput from "./components/Pages/06DailyInput";
// import ResultSave from "./components/Pages/Result/ResultSave";
// import ResultFail from "./components/Pages/Result/ResultFail";
import Amount from "./components/Pages/09Amount";
import UserRank from "./components/Pages/Rank/11UserRank";
import WishListRank from "./components/Pages/Rank/10WishListRank";
import SelectStore from "./components/Store/01SelectStore";
import Recommand from "./components/Store/02Recommand";
// import StoreDetail from "./components/Store/03StoreDetail";
// import KaKaoLogin from "./components/Accounts/KaKaoLogin";
import KakaoSignUp from "./components/Accounts/KaKaoSignUp";
// import StoreDetail from "./components/Store/03StoreDetail";

import Survey from "./components/Accounts/Survey";
import Success from "./components/UserPage/04Success";

import ResultPage from "./components/Pages/Result/07ResultPage";

const Fullpage = () => (
  <ReactFullpage
    //fullpage options
    licenseKey={"YOUR_KEY_HERE"}
    scrollingSpeed={1000} /* Options here */
    navigation={true} // 오른쪽 네비게이션바 활성화
    verticalCentered={false} // css 풀린건가..?
    controlArrows={false}
    menu={'#menu'}
    anchors={['firstPage', 'secondPage', 'thirdPage', 'fourthPage', 'fifthPage', 'sixthPage']}
    render={({ state, fullpageApi }) => {
      return (
        <ReactFullpage.Wrapper>
          <div className="section">
            <Greeting />
          </div>
          <div className="section">
            <Service />
          </div>
          <div className="section">
            <Survey />
          </div>
          <div className="section">
            <MonthlyInput />
          </div>
          <div className="section">
            <DailyInput />
          </div>
          <div className="section">
            <div className="slide">
              <ResultPage fullpage_api={fullpageApi} />
            </div>
            <div className="slide">
              <UserRank fullpage_api={fullpageApi} />
            </div>
          </div>

          <div className="section">
            <Amount />
          </div>
          <div className="section">
            <SelectStore />
          </div>
          <div className="section">
            <Recommand />
          </div>
        </ReactFullpage.Wrapper>
      );
    }}
  />
);

export default Fullpage;
