import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
    title: 'Components/Button',
    component: ButtonComponent,
    tags: ['autodocs'],
    argTypes: {
        variant: {
            control: 'select',
            options: ['primary', 'secondary', 'tertiary', 'danger'],
        },
        size: {
            control: 'select',
            options: ['sm', 'md', 'lg'],
        },
        icon: {
            control: 'text',
        },
    },
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = {
    args: {
        label: 'Primary Button',
        variant: 'primary',
        size: 'md',
    },
};

export const Secondary: Story = {
    args: {
        label: 'Secondary Button',
        variant: 'secondary',
        size: 'md',
    },
};

export const Tertiary: Story = {
    args: {
        label: 'Tertiary Button',
        variant: 'tertiary',
        size: 'md',
    },
};

export const Danger: Story = {
    args: {
        label: 'Danger Button',
        variant: 'danger',
        size: 'md',
    },
};

export const Large: Story = {
    args: {
        label: 'Large Button',
        size: 'lg',
    },
};

export const Small: Story = {
    args: {
        label: 'Small Button',
        size: 'sm',
    },
};

export const WithIcon: Story = {
    args: {
        label: 'Button with Icon',
        icon: 'pi pi-check',
    },
};

export const Loading: Story = {
    args: {
        label: 'Loading...',
        loading: true,
    },
};

export const Disabled: Story = {
    args: {
        label: 'Disabled Button',
        disabled: true,
    },
};
