let component = ReasonReact.reducerComponent("World");

let initialState = {};

let make = _children => {...component, initialState: () => initialState};