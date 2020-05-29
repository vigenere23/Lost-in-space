import { IsNotEmpty } from 'class-validator'
import { Position } from '../shared/position'


export class PlayerInfos {
    @IsNotEmpty()
    position: Position
    
    @IsNotEmpty()
    angle: number
}
