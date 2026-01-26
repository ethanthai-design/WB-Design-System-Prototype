import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';

/**
 * WB Button Component
 * 
 * A customizable button component built on PrimeNG with design token styling.
 * Supports multiple variants, sizes, and states.
 * 
 * @example
 * ```html
 * <wb-button label="Click me" variant="primary" size="md"></wb-button>
 * ```
 */
@Component({
  selector: 'wb-button',
  standalone: true,
  imports: [CommonModule, ButtonModule],
  templateUrl: './button.component.html',
  styleUrl: './button.component.scss'
})
export class ButtonComponent {
  /**
   * Button label text
   */
  @Input() label: string = 'Button';

  /**
   * Button variant style
   */
  @Input() variant: 'primary' | 'secondary-color' | 'secondary-gray' | 'tertiary-color' | 'tertiary-gray' | 'danger' = 'primary';

  /**
   * Button size
   */
  @Input() size: 'xs' | 'sm' | 'md' | 'lg' = 'md';

  /**
   * Disabled state
   */
  @Input() disabled: boolean = false;

  /**
   * Loading state
   */
  @Input() loading: boolean = false;

  /**
   * Icon name (PrimeIcons)
   */
  @Input() icon?: string;

  /**
   * Icon position
   */
  @Input() iconPos: 'left' | 'right' = 'left';

  /**
   * Full width button
   */
  @Input() fullWidth: boolean = false;
}
