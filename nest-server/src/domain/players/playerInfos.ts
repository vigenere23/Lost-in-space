import { IsNotEmpty } from 'class-validator'
import { Position } from '../position'


export class PlayerInfos {
    @IsNotEmpty()
    position: Position
    
    @IsNotEmpty()
    angle: Number
}
