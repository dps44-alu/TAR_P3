
"use strict";

let PowerSystemEvent = require('./PowerSystemEvent.js');
let VersionInfo = require('./VersionInfo.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let ControllerInfo = require('./ControllerInfo.js');
let Sound = require('./Sound.js');
let CliffEvent = require('./CliffEvent.js');
let KeyboardInput = require('./KeyboardInput.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let Led = require('./Led.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let ScanAngle = require('./ScanAngle.js');
let ButtonEvent = require('./ButtonEvent.js');
let SensorState = require('./SensorState.js');
let ExternalPower = require('./ExternalPower.js');
let MotorPower = require('./MotorPower.js');
let BumperEvent = require('./BumperEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let DigitalOutput = require('./DigitalOutput.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');

module.exports = {
  PowerSystemEvent: PowerSystemEvent,
  VersionInfo: VersionInfo,
  RobotStateEvent: RobotStateEvent,
  ControllerInfo: ControllerInfo,
  Sound: Sound,
  CliffEvent: CliffEvent,
  KeyboardInput: KeyboardInput,
  DigitalInputEvent: DigitalInputEvent,
  Led: Led,
  WheelDropEvent: WheelDropEvent,
  ScanAngle: ScanAngle,
  ButtonEvent: ButtonEvent,
  SensorState: SensorState,
  ExternalPower: ExternalPower,
  MotorPower: MotorPower,
  BumperEvent: BumperEvent,
  DockInfraRed: DockInfraRed,
  DigitalOutput: DigitalOutput,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingAction: AutoDockingAction,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingResult: AutoDockingResult,
  AutoDockingFeedback: AutoDockingFeedback,
};
