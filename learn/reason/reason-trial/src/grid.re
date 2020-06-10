type element =
  | Empty
  | Obstacle;

type row = list(element);

type grid = list(row);

let component = ReasonReact.statelessComponent("Grid");

let make = (~grid: grid) => {
  ...component
}
