import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/Navigation/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import MainPage from './components/mainPage'
import { authenticate } from './store/session';
import Posts from './components/MainPage-Posts';


function App() {
  const [loaded, setLoaded] = useState(false);

  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  // // added here
  // useEffect(()=>{
  //   dispatch()
  // }, [dispatch])

  if (!loaded) {
    return null;
  }


  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/' exact={true} >
          <MainPage />
        </ProtectedRoute>
        <Route>
          <h2>Page Not Found</h2>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
